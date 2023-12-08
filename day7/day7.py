def read_file():
    with open("day7/source.txt", "r") as file:
        return file.read()


def problem_1():
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"][
            ::-1]
    hands = []
    bids = []
    scores = []
    # 25 is five of a kind,
    # 17 is 4 oak,
    # 13 is full house,
    # 11 is 3 oaf,
    # 9 is 2 pairs,
    # 7 is one pair,
    # 5 is high card

    file_contents = read_file()
    for line in file_contents.splitlines():
        hand, bid = line.split(" ")
        score = 0
        for card in hand:
            score += hand.count(card)
        hands.append(hand)
        bids.append(int(bid))
        scores.append(int(score))

    ranks = []
    sorted_scores = sorted(scores)
    for index, (hand, bid, score) in enumerate(zip(hands, bids, scores)):
        if count := scores.count(score) == 1:
            ranks.append(sorted_scores.index(score) + 1)
        else:
            matching_score_indices = [index for index, val in enumerate(scores) if val == score]
            hand_relative_rank = 0
            for matching_index in matching_score_indices:
                if matching_index == index:
                    continue
                for card_1, card_2 in zip(hands[index], hands[matching_index]):
                    if cards.index(card_1) > cards.index(card_2):
                        hand_relative_rank += 1
                        break
                    elif cards.index(card_1) < cards.index(card_2):
                        break
            ranks.append(sorted_scores.index(score) + 1 + hand_relative_rank)

    total = 0
    for bid, rank in zip(bids, ranks):
        total += bid * rank
    print(f"Problem 1 result: {total}")


def problem_2():
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][
            ::-1]
    hands = []
    bids = []
    scores = []
    # 25 is five of a kind,
    # 17 is 4 oak,
    # 13 is full house,
    # 11 is 3 oaf,
    # 9 is 2 pairs,
    # 7 is one pair,
    # 5 is high card

    file_contents = read_file()
    for line in file_contents.splitlines():
        hand, bid = line.split(" ")
        hands.append(hand)
        bids.append(int(bid))
        counts = [hand.count(card) for card in hand if card != "J"]
        max_card_count = max(counts) if counts else 0
        min_card_count = min(counts) if counts else 0
        score = 0
        J_count = hand.count("J")
        if J_count == 5 or J_count == 4:
            score = 25
        elif J_count == 3:
            for card in hand:
                if hand.count(card) == 2:
                    score = 25
                    break
                elif hand.count(card) == 1:
                    score = 17
                    break
        elif J_count == 2:
            for card in hand:
                if hand.count(card) == 3:
                    score = 25
                    break
                elif hand.count(card) == 2 and card != "J":
                    score = 17
                    break
                elif hand.count(card) == 1:
                    if cards.count(card) == max_card_count:
                        score = 11
                        break
        elif J_count == 1:
            for index, card in enumerate(hand):
                if hand.count(card) == 4:
                    score = 25
                    break
                elif hand.count(card) == 3:
                    score = 17
                    break
                elif hand.count(card) == 2:
                    if hand.count(card) == min_card_count:
                        score = 13
                    else:
                        score = 11
                    break
                elif card != "J":
                    if cards.count(card) == max_card_count:
                        score = 7
                        break
        else:
            for card in hand:
                score += hand.count(card)
        scores.append(int(score))

    ranks = []
    sorted_scores = sorted(scores)
    for index, (hand, bid, score) in enumerate(zip(hands, bids, scores)):
        if scores.count(score) == 1:
            ranks.append(sorted_scores.index(score) + 1)
        else:
            matching_score_indices = [index for index, val in enumerate(scores)
                                      if val == score]
            hand_relative_rank = 0
            for matching_index in matching_score_indices:
                if matching_index == index:
                    continue
                for card_1, card_2 in zip(hands[index], hands[matching_index]):
                    if cards.index(card_1) > cards.index(card_2):
                        hand_relative_rank += 1
                        break
                    elif cards.index(card_1) < cards.index(card_2):
                        break
            ranks.append(sorted_scores.index(score) + 1 + hand_relative_rank)

    total = 0
    for bid, rank in zip(bids, ranks):
        total += bid * rank
    print(f"Problem 2 result: {total}")


def run():
    print("Day 7")
    problem_1()
    problem_2()