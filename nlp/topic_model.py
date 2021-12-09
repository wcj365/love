#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://zhuanlan.zhihu.com/p/347738635
# https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/
# https://datascienceplus.com/evaluation-of-topic-modeling-topic-coherence/

import os
import re
#import matplotlib.pyplot as plt
#import pandas as pd
import gensim
from gensim import corpora, models
import pyLDAvis
import pyLDAvis.gensim_models 
import jieba

CN_STOPWORDS = "cn_stopwords.txt"
MY_STOPWORDS = "my_stopwords.txt"

def topic_model(doc_list, num_topics):

    dictionary = corpora.Dictionary(doc_list)
    bow_corpus = [dictionary.doc2bow(doc) for doc in doc_list]

    # LDA using Bag of Words (BoW)
    lda_model = models.LdaMulticore(
        corpus=bow_corpus, 
        num_topics=num_topics, 
        id2word=dictionary, 
        passes=10, 
        workers=2,
        random_state=100
    )

    # Creating Topic Distance Visualization.
    viz = pyLDAvis.gensim_models.prepare(
        lda_model, 
        corpus=bow_corpus, 
        dictionary=dictionary
    )
    
    # Compute Coherence Score
    coherence_model = models.CoherenceModel(
            model=lda_model, 
            texts=doc_list,
            dictionary=dictionary, 
            coherence='c_v')
    c_v = coherence_model.get_coherence()

    # Compute Coherence Score
    coherence_model = models.CoherenceModel(
            model=lda_model, 
            texts=doc_list,
            dictionary=dictionary, 
            coherence='u_mass')

    u_mass = coherence_model.get_coherence()

    # Compute Perplexity - a measure of how good the model is. lower the better.
    perplexity = lda_model.log_perplexity(bow_corpus)

    return lda_model, viz, c_v, u_mass, perplexity



def optimal_topics(doc_list, start, stop, step):

    x = list(range(start, stop, step))
    y = []
    z = []
    u = []
    for i in x:
        lda_model, viz, c_v, u_mass, perplexity = topic_model(doc_list, i)
        y.append(c_v)
        z.append(u_mass)
        u.append(perplexity)
        print(f"# Topics: {i} - Perplexity: {perplexity} - c_v: {c_v} - u_mass: {u_mass}") 

    return [x,y,z,u]


def plot_metrics(metrics):

    fig, axs = plt.subplots(2, figsize=(8,4), sharex=True) 
    axs[0].plot(metrics[0],metrics[1])
    axs[1].plot(metrics[0], metrics[2])
    fig.savefig("../images/optimal_topics2.png")


def exp8_optimal():

    df_good, _ = prepare_data("../data/exp8_params.csv")
    metrics = optimal_topics(df_good["document"])
    plot_metrics(metrics)

def usecase_1(folder, subfolders):
    doc_list = []
    for sub in subfolders:
        full_path = folder + "/" + sub
        files = os.listdir(full_path)

        for file in files:
            if file.startswith("README") or not file.endswith(".md"):    
                continue 

            with open(full_path + "/" + file, "r") as f_read:
                lines = f_read.readlines()

          # strinfo = re.compile('[0-9a-zA-Z]|京东|美的|电热水器|热水器|')               
            strinfo = re.compile('[0-9a-zA-Z]')
            content_list = []
            for line in lines:
                if line.startswith("注") or line.startswith("附"):
                    break
                if line.startswith("#") or line.startswith("!"):
                    continue
                else:
                    content_list.append(strinfo.sub('', line))

            content = " ".join(content_list)

            cn_path = open(CN_STOPWORDS, 'r',encoding='UTF-8')
            cn_stop = cn_path.readlines()
            cn_stop = [x.replace('\n', '') for x in cn_stop]

            my_path = open(MY_STOPWORDS, 'r',encoding='UTF-8')
            my_stop = my_path.readlines()
            my_stop = [x.replace('\n', '') for x in my_stop]

            word_list = jieba.lcut(content,cut_all=False)   # 结巴词库切分词 精准模式
            new_list = []
            for word in word_list:
                if len(word.strip()) == 0 or word in my_stop + cn_stop:
                    continue
                else:
                    new_list.append(word)
            print(new_list)
            print("\n\n")
            doc_list.append(new_list)

    return doc_list


def main():

#    doc_list = usecase_1("../src/classic_poems",["wu_jue", "qi_jue", "wu_lv", "qi_lv"])
#    doc_list = usecase_1("../src/modern_poems",["birthday", "homesick", "love", "nature", "solitude", "wisdom"])
    doc_list = usecase_1("../src/proses",["econ_tech", "fun", "health", "life", "poetry", "politics","wisdom", "wordgame"])
    lda_model, viz, _, _, _ = topic_model(doc_list, 5)
    pyLDAvis.save_html(viz, "lda.html")

#    optimal_topics(doc_list, 2, 30, 1)


if __name__ == "__main__":
    main()

