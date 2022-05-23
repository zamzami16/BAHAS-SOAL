a = """
---
![](source/PAT FIS-X 2022_Page{}.png)
"""

with open(r'soal_fisika_kelas_10_PAT.md') as f:
    for i in range(1, 22):
        f.write(a.format(i))
    f.close()