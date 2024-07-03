import mod
import read_csv
import charts

def run():
    data = read_csv.read_csv('data.csv')
    
    data = list(filter(lambda i:i['Continent'] == 'South America',data))
  
    continente = list(map(lambda i : i['Country/Territory'],data))
    porcentaje = list(map(lambda i : i['World Population Percentage'],data))
 
    charts.generate_pie_chart(continente,porcentaje)
    
    
    country = input("Type Country => ")
    result = mod.population_by_country(data,country)
    
    if len(result)>0:
        country = result[0]
        labels,values = mod.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'],labels,values)

    
if __name__ == '__main__':
    run()
