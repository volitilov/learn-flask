# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#  контекст приложения

current_app
# экземпляр активного приложения

g 
# объект, который может использоваться приложением как временное 
# хранилище в процесе обработки запроса. Эта переменная сбрасывается 
# в исходное состояние для каждого нового запроса


app.push()
# установить контект  

app.pop()
# удалить контекст



# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#  контекст запроса

app.test_request_context()
# создаёт контекст запроса, как будто flask обрабатывает запросы

app.request_context()
# 

request
# объект запроса, включающий содержимое HTTP-запроса, отправленного 
# клиентом

session
# сеанс пользователя - словарь, который может использоваться 
# приложением для сохранения значений между запросами

