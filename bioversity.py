#!/usr/bin/python
#coding: utf-8
import random
from twython import Twython

consumer_key = ""
consumer_key_secret = ""
access_token = ""
access_token_secret = ""

twitter = Twython(consumer_key, consumer_key_secret, access_token, access_token_secret)

ADJECTIVE = ["Trans", "Shy", "Asexual", "Neuroatypical", "Plural", "Cute", "19-year-old", "Cuddly", "Music-loving", "Funny", "Warm-hearted", "Multiple", "Silly", "Goofy", "Awkward", "Autistic", "Radical"]
DESCRIPTOR = ["girl", "student", "catgirl", "wannabe", "woman", "SJW", "activist", "punk", "magical girl", "punk rock princess", "witch", "protagonist", "clutz"]
ACTION = ["studying software engineering", "doing the best I can", "trying to change the world", "fighting for my friends", "befriending nice people", "lurking on a forum somewhere", "relearning empathy and kindness", "eating Chinese food", "probably baking desserts", "singing too loudly in the shower", "stumbling over code", "stubbing her toe", "watching anime", "eating Italian food", "eating sweets", "curled up, asleep"]
RELATIONSHIP = [
    "wife to @enbykid",
    "headmate to @kinuko_chan & @SomethingCole",
    "DPS to @tteugeo",
    "adventuring partner to @m1sp",
    "programming fangirl to @FioraAeterna",
    "sister to @MinaZenunim",
    "mom to everybody",
    "kouhai to @Dirk_Gently",
    "senpai to @winocm_plus",
    "support to @hoodiejoy",
    "healer to @SeventhRondo",
    "brand witch to @SaulKewl",
    "future roommate to @plus_chan",
    "bestie to @RijoPorter",
    "terror to #GamerGate",
    "antagonist to bigots",
    "mistress of memes",
    "scourge to America",
    "winner of Mario Kart",
    "mayor of Animal Crossing"
]

def generate(max_length):
    terminator = "Your friend"
    length_tolerance = 10

    for list_to_shuffle in [ADJECTIVE, DESCRIPTOR, ACTION, RELATIONSHIP]:
        random.shuffle(list_to_shuffle)

    next_relationship = RELATIONSHIP.pop().capitalize()

    bio = "{0} {1} {2}. {3}".format(ADJECTIVE.pop(), DESCRIPTOR.pop(), ACTION.pop(), next_relationship)

    while len(bio) < (max_length - length_tolerance):
        if len(RELATIONSHIP) == 0:
            return attempt
        next_relationship = RELATIONSHIP.pop()
        attempt = "{0}, {1}. {2}.".format(bio, next_relationship, terminator)
        if len(attempt) > max_length:
            continue
        elif len(attempt) > max_length - length_tolerance:
            return attempt
        bio += ", {0}".format(next_relationship)

desc = generate(140)
twitter.update_profile(description=desc)

# EOF
