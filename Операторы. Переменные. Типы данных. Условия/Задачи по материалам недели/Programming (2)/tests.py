from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["5.0\n0.0\nmod","Деление на 0!"],["-12.0\n-8.0\n*","96.0"],["5.0\n10.0\n/","0.5"]])