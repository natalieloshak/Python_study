name = "Наталія"
address = "проспект С.Бандери 26Б"
service = "манікюр з покриттям"
time = "25 квітня о 15:00"
smile1 = "💅"
smile2 = "❤"
sms = f"Шановна {name}, ми Вас очікуємо на {service} {smile1}. \nАдреса:{address}. \nДата: {time}. \nДо зустрічі! {smile2}"

import templates_practice

sms2 = templates_practice.SMS_WARNING_MSG.format(name=name, service=service, time=time)
pass
