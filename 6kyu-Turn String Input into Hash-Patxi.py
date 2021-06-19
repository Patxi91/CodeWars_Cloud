def str_to_hash(st):
    return {ele[0:ele.find('=')]: int(ele[ele.find('=')+1:]) for ele in st.split(', ')} if st != "" else {}
