def proofread(st):
    words = st.lower().split()
    for i in range(len(words)):
        if 'ie' in words[i]:
            words[i] = words[i].replace('ie', 'ei')
    corrected_ie = ' '.join(words).capitalize()
    sentences = corrected_ie.split('.')
    corrected_text = '. '.join([sentence.strip().capitalize() for sentence in sentences])
    return corrected_text.strip()
