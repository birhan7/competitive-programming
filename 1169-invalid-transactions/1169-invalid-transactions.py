class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        memo = defaultdict(list)
        invalid = set()
        for index, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            amount, time = int(amount), int(time)

            memo[name].append((time, city, index))
            if amount > 1000:
                invalid.add(index)

            for prev_time, prev_city, prev_idx in memo[name]:
                if abs(time - prev_time) <= 60 and prev_city != city:
                    invalid.add(index)
                    invalid.add(prev_idx)

        return [transactions[i] for i in invalid]
        

        