
def species_cleaner(species): 
    import re 
    shark_match = re.search(r'(white|tiger|bull|reef|lemon|hammerhead|blacktip|nurse|whale|blue|bronze|whaler|thresher|porbeagle|spinner|sandbar|tawny nurse|wobbegong|withe tip)', species, flags=re.IGNORECASE)

    if shark_match:
        if shark_match.group(1).lower() in ['bronze', 'whaler']:
            return 'Whaler bronze shark'
        else:
            return shark_match.group(1).capitalize() + ' shark'
    else:
        return 'Generic Shark'
    



def source_cleaner(source):
    import re
    source_match = re.search(r'(Petersohn|Creswell|Collier|Peake|Gifford|Myatt|Ritter|Levine|Vorenberg|Fouda|Van Grevelynghe|Orlando Sentinel|Lopes)', source, flags=re.IGNORECASE)
    if source_match: 
        return source_match.group(1).capitalize()
    else:
        return 'Unknown Source'
    




def contar_palabras(df, columna_texto, top_n=1000):
    import regex as re 
    import pandas as pd
    all_text = ' '.join(df[columna_texto].astype(str))
    words = [word for word in re.sub(r'[^a-zA-Z\s]', '', all_text.lower()).split() if len(word) > 3 and word != 'gsaf']
    word_freq_df = pd.DataFrame({'Palabra': words}).value_counts().reset_index(name='Frecuencia')
    return word_freq_df.head(top_n)



def limpiar_nan(dataframe, umbral_f=0.5, umbral_c=0.70):
    dataframe = dataframe[dataframe.isnull().sum(axis=1) <= umbral_f * dataframe.shape[1]]
    dataframe = dataframe[dataframe.columns[dataframe.isnull().mean() <= umbral_c]]

    return dataframe


def activity_cleaner(activity): 
    import re 
    activity_match = re.search(r'(Paddling|Swimming|Walking|Feeding sharks|Scuba diving|Fishing|Paddle-skiing|Stand-Up Paddleboarding|Wading|Spearfishing|Night bathing|Kayaking|Snorkeling|SUP|Kayaking|Body boarding|Scuba Diving|Surf|Floating|SUP Foil boarding|Kite surfing|Floating in tube|Standing|Diving|Teasing a shark|Paddle boarding|Kayak Fishing|Surf-skiing|Scallop diving on hookah|Body boarding |Playing in the water|Body Boarding|Boogie boarding|Playing|Standing / Snorkeling|Hand feeding sharks|Rowing|Shark fishing|Fishing|Kayaking|Body surfing|Kitesurfing|Kiteboarding|Diving|snorkeling|Diving for Abalone|Casting a net|Cleaning fish|Boogie Boarding|Playing in the surf|Kite boarding|Fishing|Bodyboarding|Swimming or boogie boarding|Free diving |Sitting in the water|Free diving / spearfishing)', activity, flags=re.IGNORECASE)

    if activity_match:
        return activity_match.group(1).capitalize() 
    else:
        return 'Otros'
    


def asignar_estacion(dataframe):
    def obtener_estacion(month, hemisphere):
        if hemisphere == 'HN':
            if 3 <= month <= 5:
                return 'Primavera'
            elif 6 <= month <= 8:
                return 'Verano'
            elif 9 <= month <= 11:
                return 'Otoño'
            else:
                return 'Invierno'
        elif hemisphere == 'HS':
            if 9 <= month <= 11:
                return 'Primavera'
            elif 12 <= month <= 2:
                return 'Verano'
            elif 3 <= month <= 5:
                return 'Otoño'
            else:
                return 'Invierno'
        else:
            return 'Desconocido'

    dataframe['Season'] = dataframe.apply(lambda row: obtener_estacion(row['Mes'], row['Hemisferio']), axis=1)
    return dataframe




def extraer_mes(fecha_string):
    from datetime import datetime
    try:
        fecha_objeto = datetime.strptime(fecha_string, "%d-%b-%Y")
        mes_numero = fecha_objeto.month
        
        return mes_numero
    except ValueError:
        return None
    

def asignar_hemisferio(pais):
    hemisferio_sur = ['BRAZIL', 'AUSTRALIA', 'COSTA RICA', 'MALDIVES', 'SOUTH AFRICA', 'NEW ZEALAND', 'FRENCH POLYNESIA', 'NEW CALEDONIA', 'ECUADOR', 'REUNION', 'JAMAICA', 'PAPUA NEW GUINEA', 'SEYCHELLES', 'MOZAMBIQUE', 'FIJI', 'TONGA', 'VANUATU', 'VENEZUELA', 'TURKS & CAICOS', 'NEW BRITAIN', 'PALAU', 'SOLOMON ISLANDS', 'FEDERATED STATES OF MICRONESIA', 'GREECE', 'SENEGAL', 'ARGENTINA', 'EL SALVADOR']
    return 'HS' if pais.upper() in hemisferio_sur else 'HN'