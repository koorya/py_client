# py_client
Этот клиент является демонстрационным. Он при запуске посылает ZMQ запрос ПВУ со словом "capture", ожидая в ответ получить изображение с камеры обработанное нейросетью. 
После принятия изображения обратно, он отображает его в окне на несколько секунд, затем закрывает окно и посылает ПВУ команду kill, а затем завершается и сам.