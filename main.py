from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from statics import function


class MainContainer(BoxLayout):

    search = ObjectProperty()
    cityName = ObjectProperty()
    weatherIcon = ObjectProperty()
    temp = ObjectProperty()
    feelTemp = ObjectProperty()
    weatherDescription = ObjectProperty()
    backWeather = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weatherIcon.color = (0,0,0,0)
        with self.canvas.before:
            self.rect = Rectangle(source='statics/clouds.jpg')

    def on_pos(self, *args):
        # update Rectangle position when MazeSolution position changes
        self.rect.pos = self.pos

    def on_size(self, *args):
        # update Rectangle size when MazeSolution size changes
        self.rect.size = self.size

    def setWeather(self):
        rain = ['Дождь', 'Сильный дождь', 'небольшой дождь', 'сильный дождь', 'моросящий дождь']
        try:
            weather = function.find(self.cityName.text)
            print(weather)
            self.weatherIcon.source = weather['icon_source']
            self.temp.text = weather['temp_real']
            self.feelTemp.text = weather['temp_feels']
            self.weatherIcon.color = (1,1,1,1)
            description = weather['description']
            descriptionFinal = ''
            tmp = ''
            desc = list(description.split())
            #print(desc[1:])
            if len(desc) == 1:
                self.weatherDescription.text = weather['description']
            elif len(desc) > 1:
                descriptionFinal = desc[0] + '\n'
                for i in desc[1:]:
                    tmp += i + ' '
                descriptionFinal += tmp
                self.weatherDescription.text = descriptionFinal
            for i in desc:
                if i == 'дождь':
                    self.rect.source = 'statics/rain.jpg'
                elif i == 'ясно':
                    self.rect.source = 'statics/clear.jpg'
                elif i == 'гроза':
                    self.rect.source = 'statics/storm.jpg'
                elif i == 'туман':
                    self.rect.source = 'statics/steam.jpg'
                elif i == 'пасмурно':
                    self.rect.source = 'statics/mainlyCloudy.jpg'
                elif i == 'облачно' or i == 'прояснениями' or i == 'облачность':
                    self.rect.source = 'statics/cl2.jpg'
                else:
                    self.rect.source = 'statics/clouds.jpg'
        except KeyError:
            self.weatherDescription.text = 'Введите\n город'
            self.rect.source = 'statics/error.jpg'

class WeatherApp(App):
    def build(self):
        Window.clearcolor = (0.8, 0.8, 0.8, 1)
        Window.size = (700, 350)
        return MainContainer()


if __name__ == '__main__':
    WeatherApp().run()