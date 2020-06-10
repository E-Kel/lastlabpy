

DB = {
    "Харьков":[27,"Солнечно"],
    "Киев":[25,"Облачно"],
    "Лондон":[22,"Ливни"],
    "Нью-Йорк":[28,"Временами грозы"]
}

class Weather_db:

    @staticmethod
    def update_info(key, temp=None, description=None):
        DB.update({key:[temp,description]})

class City:
    def __init__(self, city):
        self.__city = city
        try:
            self.__weather = DB[city]
        except:
            print("Invalid value or this city is not tracking yet")
    def show_weather(self):
        print("Температура: {0}\n" \
                "В общем: {1}\n".format(self.__weather[0], self.__weather[1]))

    @staticmethod
    def set_city():
        city = input("Enter city name : ")
        return City(city)


def main():
    Weather_db.update_info("Вашингтон")
    Weather_db.update_info("Запорожье", 23, "Пасмурно")
    while (True):
        c = City.set_city()
        c.show_weather()


if __name__ == '__main__':
    main()