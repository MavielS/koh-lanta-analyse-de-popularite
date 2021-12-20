import pandas as pd
import pickle


NOMS_CANDIDATS = ['Freddy', 'Teheuira', 'Patrick', 'Alexandra', 'Cindy', 'Claude', 'Karima', 'Jade', 'Maxime', 
                  'Laurent', 'Candice', 'Sam', 'Clementine', 'Ugo', 'Namadia', 'Christelle', 'Coumba', 'Loic', 
                  'Clemence', 'Phil', 'Alix', 'Denis']

def get_all_tweets_by_name(nom, from_em=0, until_em=15):
    '''
    Renvoie toutes les données pour un candidat précis
    '''
    results= pd.DataFrame()
    for num in range(from_em, until_em+1):
        path = f'./data_jugement/em{num}/'
        df = pd.read_pickle(path + nom.lower() + '.pickle')
        results = pd.concat([results, df])
    return results.drop_duplicates(subset='content', )


def get_all_tweets(nom_candidats, from_em=0, until_em=15):
    '''
    Renvoie tous les tweets disponibles
    '''
    results = pd.DataFrame()
    for nom in nom_candidats:
        results = pd.concat([results, get_all_tweets_by_name(nom, from_em, until_em)])
        
    return results

def surnoms_trouves(nom, until_em = 15):
    '''
    Renvoie tous les surnomss trouvés pour un candidat jusqu'à l'épisode @until_em
    '''
    result = []
    for ind in range(0,until_em+1):
        path = f'./data_jugement/surnoms/surnoms_em{ind}.pickle'
        d=pickle.load(open(path,'rb'))
        result.append(d[nom].tolist())
    return list(set(sum(result, []))), result