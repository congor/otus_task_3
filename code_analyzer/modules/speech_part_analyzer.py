import nltk
from modules.common_utilities import make_list_flat

nltk.download('averaged_perceptron_tagger')

def filter_words(names, part_of_speech):
    filtered_words = [word_from_name(name, part_of_speech) for name in names]
    return make_list_flat(filtered_words)

def word_from_name(name, part_of_speech):
    splitted_name = name.split('_')
    words = [word for word in splitted_name if word]
    attached_tags = nltk.pos_tag(words)    
    return [attached_tag[0] for attached_tag in attached_tags if part_of_speech in attached_tag[1]]

def check_part_of_speech_analysis_availability(part_of_speech):
    parts_of_speech = get_parts_of_speech_dictionary()
    if part_of_speech in parts_of_speech:
        return True
    else:        
        return False

def get_parts_of_speech_dictionary():
    parts_of_speech = {'NN': 'nouns',
                       'VB': 'verbs'}
    return parts_of_speech