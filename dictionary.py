def dictionary():
    """
    Function implements dictionary
    :return: operations performed on dictionary data structure
    """
    try:
        tel = {'loki': 3214, 'son': 1234}
        print("Dictionary tel is : ", tel)

        # Adding key 'per' having value 7894 in dictionary tel
        tel.update([('per', 7894)])
        tel.update({'sdf': 2345})
        print("After adding 2 keys dictionary tel is : ", tel)

        # get value of a particular key
        print("Value of key 'loki' is : ", tel.get('loki'))
        print("When key value pair is not present : ", tel.get('vom', 'Key Not Available'))
        print("Default value when key is not present : ", tel.get('vom'))

        # copy tel to tel2
        tel2 = tel.copy()
        print("Copied dictionary tel in tel2 is : ", tel2)
        print("tel2 dictionary items are : ", tel2.items())
        print("Keys in tel2 is : ", tel2.keys())
        print("Values in tel2 is : ", tel2.values())

        # deleting element in dictionary
        del[tel2['per']]
        print("After deleting key 'per' tel2 is : ", tel2)

        # clearing dictionary
        tel2.clear()
        print("After clearing tel2 is : ", tel2)

    except Exception as err:
        print(err)


if __name__ == "__main__":
    print("Dictionary operations are : ")
    dictionary()
