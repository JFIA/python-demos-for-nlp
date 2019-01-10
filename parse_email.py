

def parse_email(email):
    count_url = 0
    count_atta = 0
    email_feature = [0, 0]
    for item in email:
        if ('<head>' in item) | ('<body>' in item):
            email_feature[0] = 1
        if ('<script>') in item:
            email_feature[1] = 1
        if ('http://') in item:
            count_url += 1
        if 'Content-Disposition: attachment' in item:
            count_atta += 1
    email_feature.append(count_url)
    email_feature.append(count_atta)
    return email_feature


def build_email_feature(pure_email, vec_feature):   # vec_feature是word2vec产生的特征值。
    email_feature = []
    for item in pure_email:
        feature = parse_email(item)
        email_feature.append(feature)
    for i in range(len(email_feature)):
        for j in range(len(vec_feature[i])):
            email_feature[i].append(vec_feature[i][j])
    return email_feature
