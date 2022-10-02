# creating string list of sentences
# take input from user and input convert in to lower case
# match the most relevant search and give output in descending order


def matching(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == '__main__':
    ls = ['this is good', 'python is good', 'python used to write program and python widely used for its multi functionality']
    query = input("Enter your search keyword \n")

    scores = [matching(query, sentence) for sentence in ls]
    # print(scores)
    SortsentScore = [sentscore for sentscore in sorted(zip(scores, ls), reverse=True)]
    # zip is used to mix one list item with another list items considering theor index value
    # a =[1,5,6]
    # b=[2,65,8]
    # zip(a,b) ==== [(1,2) (5,65) (6,8)]
    # print(SortsentScore)

    # below line return score and item in list of SentscoreScore
    # for score, item in SortsentScore:
        # print(f' \'{item}\':  is found with score of {score}')

    # below code get only search result
    for score, item in SortsentScore:
        print(item)