# = = = = Variables and Some Arithmetic = = = =
a = 883
b = 813
result = a ** 2 + b ** 2
print(f'{a}^2 + {b}^2 = {result}')

# = = = = Strings and Lists = = = =
s = 'nzQOKluHXSr3H87ABiBzSktuKzvd86zyvs4UUEPU4o7aV5hJwXv5Ozu8SX4wDL3OColumbairiaL5aIqGsR5KzPAgHY6ImzBV4M8fparvus4MTr16em7k7t3w8895GmRbW3XuG0Nv2m0nVFhTIKgbMKidVpmvNwBiNvq7vFfatFwPXpqQHSuPzIp5eV9.'
first_start = 64
first_end = 70
second_start = 101
second_end = 106

# Note: end position is not inclusive, so add 1
first = s[first_start:first_end+1]
second = s[second_start:second_end+1]
print(f'{first} {second}')

# = = = = Conditions and Loops = = = =
a = 4157
b = 8397
sum = 0

while a <= b:
    if a % 2 == 0:
        a += 1
    else:
        pass
    sum += a
    a += 2

print(sum)

# = = = = Working with Files = = = =
# f = open('working_with_files_input.txt', "r")
# lines = f.readlines()
# f2 = open('working_with_files_output.txt', "w")
#
# for count, line in enumerate(lines):
#     if count % 2 == 1:
#         f2.write(line)

# = = = = Dictionaries = = = =
s = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
l = s.split(' ')
d = {}
c = 0

for word in l:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

for word in d:
    print(f'{word} {d[word]}')
