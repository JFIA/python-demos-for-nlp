from parse_email import *
from word_to_vec import *
from pure_email import *
from sanitiser_email import *
import os


fp_spam = 'C:\\Users\\Rafel_Hu\\Desktop\\spam_corpus\\spam_2'
fp_ham = 'C:\\Users\\Rafel_Hu\\Desktop\\spam_corpus\\hard_ham'
os.chdir(fp_spam)

pure_email_spam, fail_spam = pure_email(fp_spam)
pure_email_ham, fail_ham = pure_email(fp_ham)


string_list_spam = list2string(pure_email_spam)
string_list_ham = list2string(pure_email_ham)


vocab_list_spam = sanitiser_email(string_list_spam)
vocab_list_ham = sanitiser_email(string_list_ham)

vec_feature_spam = build_feature(vocab_list_spam)
vec_feature_ham = build_feature(vocab_list_ham)


email_feature_spam = build_email_feature(pure_email_spam, vec_feature_spam)
email_feature_ham = build_email_feature(pure_email_ham, vec_feature_ham)

#print(vec_feature_ham)