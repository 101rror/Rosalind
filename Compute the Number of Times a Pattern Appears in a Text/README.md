<h2><a href="https://rosalind.info/problems/ba1a/">Compute the Number of Times a Pattern Appears in a Text</a></h2>

<p>This is the first problem in a collection of "code challenges" to accompany <a href="http://bioinformaticsalgorithms.org/"> Bioinformatics Algorithms: An Active-Learning Approach</a> by Phillip Compeau & Pavel Pevzner.</p>
<p>A <a href="https://rosalind.info/glossary/k-mer/"> k-mer </a> is a <a href="https://rosalind.info/glossary/string/">string </a> of length k. We define Count(Text, Pattern) as the number of times that a k-mer Pattern appears as a <a href="https://rosalind.info/glossary/substring/">substring </a> of Text. For example, <strong> Count(ACAACTATGCATACTATCGGGAACTATCCT, ACTAT) = 3.</strong></p>

<p>We note that <strong>Count(CGATATATCCATAG, ATA) </strong> is equal to 3 (not 2) since we should account for overlapping occurrences of Pattern in Text.</p>


<p>To compute Count(Text, Pattern), our plan is to “slide a window” down Text, checking whether each k-mer substring of Text matches Pattern. We will therefore refer to the k-mer starting at position i of Text as Text(i, k). Throughout this book, we will often use <a href="https://rosalind.info/glossary/0-based-numbering/"> 0-based indexing, </a> meaning that we count starting at 0 instead of 1. In this case, Text begins at position 0 and ends at position |Text| − 1 (|Text| denotes the number of symbols in Text). For example, if Text = GACCATACTG, then Text(4, 3) = ATA. Note that the last k-mer of Text begins at position |Text| − k, e.g., the last 3-mer of GACCATACTG starts at position 10 − 3 = 7. This discussion results in the following pseudocode for computing Count(Text, Pattern).</p>

<pre>
<strong>PatternCount(Text, Pattern)
    count ← 0
    for i ← 0 to |Text| − |Pattern|
        if Text(i, |Pattern|) = Pattern
            count ← count + 1
    return count</strong>
</pre>

<strong>Implement PatternCount</strong>

<p><strong>Given : </strong>{DNA strings}} Text and Pattern.</p>
<p><strong>Return : </strong>Count(Text, Pattern).</p>

<p>&nbsp;</p>
<p><strong class="example">Sample Dataset</strong></p>
<pre>
<strong>GCGCG
GCG</strong>
</pre>
<p><strong class="example">Sample Output</strong></p>
<pre>
<strong>2</strong>
</pre>
