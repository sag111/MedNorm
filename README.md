# Python файлы для pipeline NER + Normalization

## Как все работает?
В train.py закладываются файлы с тренировочными данными в особом sagnlpjson формате, который был введен Артемом (не было времени переписывать скрипты под обычный sagnlp, под обычный sagnlp работает только Demo.ipynb) - sagnlp_v2, в особом формате sagnlp_v2 вместо поля  entities типа dict с объектами ent идет list доступный по адресу ['objects']['MedEntity'] с теми же самыми объектами ent, за исключением того что в MedDRA у ent из sagnlp_v2 идет не PT code, а PT фраза. Опционально также подаются тестировочные и валидационные множества. Если подается тестировочное множество, то в конце будет **тест**. В train.py в параметре --meddra_path идет путь до файла meddra, он нужен для векторизатора концептов. В -res путь до сохраненной модели после обучения и сохраненного векторизатора концептов с его вложжениями концептов. В --transformer_model_path указывается путь до модели трансформера. В -load_model идет путь до предобученной модели с сохраненным векторизатором концептов. Все аргументы объяснены в train.py в полях description, кроме use_cuda и use_conceptless - ну, это вы сами знаете, для чего<br><br>
Если подается валидационный файл, то сразу подключается early_stopping с patiens 7 epochs. Валидация без concepless, как и обучение<br><br>
Если подается тестовый файл, то в конце расситывается точность на голд NER. Флаг `--use_conceptless` контролирует рассчет на тесте с concept_less и без. По умоланию без concepless.<br><br>
В `res_dir` подается папка, куда будет сохранена
- Модель CADEC_SoTa
- Векторизатор
- Вложения векторизатора
<br><br>
В `-model` подается путь до модели трансформера, которая будет учиться в сетке. Однако, если вы хотите запустить уже предобученную нормализационную модель CADEC_SoTa, то используйте `--load_model` с путью до папки с файлами, описанными выше.<br> 
## Основные файлы
1. train.py. Пример запуска: `python train.py -tr ./Demo/data/demo.json -val ./Demo/data/demo.json -ts ./Demo/data/demo.json -load_pretrained ./Model_weights/rubert_11072022_test -res ./Demo/saved_model_dir/ --use_cuda`
2. predict.py. Пример запуска: `python predict.py -p ./Demo/data/demo.json -res ./Demo/data/demo_with_predicted_meddra_ents.json -model ./Demo/saved_model_dir/`
3. norm_eval.py. Пример запуска: `python -t ./Demo/data/demo.json -p ./Demo/data/demo_with_predicted_meddra_ents.json`
## Разбивка на фолды
Скрипт create_splits.py. Без аргументов. Сплитит файлы из ./Data/Full_corps/ - RDRS, CADEC. На 5 фолдов, фолды сохраняются в ./Data/RDRS_splits и ./Data/CADEC_splits вместе с id отзывов фолдов. 
