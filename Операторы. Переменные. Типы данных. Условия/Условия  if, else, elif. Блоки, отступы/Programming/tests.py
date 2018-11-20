from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["6\n10\n8","Это нормально"],["7\n9\n10","Пересып"],["7\n9\n2","Недосып"]])