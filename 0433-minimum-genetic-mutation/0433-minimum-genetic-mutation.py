class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bases = ['A', 'C', 'G', 'T']

        queue = deque([startGene])
        seen = {startGene}
        bank = set(bank)
        breadth = 0

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                gene = queue.popleft()

                if gene == endGene:
                    return breadth

                for i in range(len(gene)):
                    for base in bases:
                        temp_gene = (
                            gene[:i] + base + gene[i + 1:]
                        )

                        if temp_gene in bank and temp_gene not in seen:
                            queue.append(temp_gene)
                            seen.add(temp_gene)

            breadth += 1

        return -1
