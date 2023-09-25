domain_file_path = 'domain.txt'
with open(domain_file_path, 'r') as file:
    domain_list = [line.strip() for line in file.readlines()]
