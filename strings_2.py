import templates_practice

name = input(templates_practice.MSG_ENTER_NAME)
# name = "Наталія"
address = "проспект С.Бандери 26Б"
service = "манікюр з покриттям"
time = "25 квітня о 15:00"
smile1 = "💅"
smile2 = "❤"
sms = f"Шановна {name}, ми Вас очікуємо на {service} {smile1}. \nАдреса:{address}. \nДата: {time}. \nДо зустрічі! {smile2}"
sms2 = templates_practice.SMS_WARNING_MSG.format(name=name, service=service, time=time)
