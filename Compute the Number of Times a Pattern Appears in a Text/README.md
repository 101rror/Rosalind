<h2><a href="https://rosalind.info/problems/ba1a/">Compute the Number of Times a Pattern Appears in a Text</a></h2>

<p>&nbsp;</p>
<p><strong class="example"></strong></p>

<p>This is the first problem in a collection of "code challenges" to accompany <a href="http://bioinformaticsalgorithms.org/"> Bioinformatics Algorithms: An Active-Learning Approach</a> by Phillip Compeau & Pavel Pevzner.</p>
<p>A <a href="https://rosalind.info/glossary/k-mer/"> k-mer </a> is a <a href="https://rosalind.info/glossary/string/">string </a> of length <strong><i>k</i></strong>. We define <i>Count(Text, Pattern)</i> as the number of times that a <i>k-mer Pattern appears</i> as a <a href="https://rosalind.info/glossary/substring/">substring </a> of <i>Text</i>. For example,</p>
<ol>
    <strong> Count(ACAACTATGCATACTATCGGGAACTATCCT, ACTAT) = 3.</strong>
</ol>
<p>We note that <strong><i>Count</i>(CGATATATCCATAG, ATA) </strong> is equal to 3 (not 2) since we should account for overlapping occurrences of <i>Pattern</i> in <i>Text</i>.</p>

<p>To compute <i>Count(Text, Pattern),</i> our plan is to “slide a window” down Text, checking whether each k-mer substring of <i>Text</i> matches <i>Pattern</i>. We will therefore refer to the <i>k</i>-mer starting at position <i>i</i> of Text as <i>Text(i, k)</i>. Throughout this book, we will often use <a href="https://rosalind.info/glossary/0-based-numbering/"> 0-based indexing, </a> meaning that we count starting at 0 instead of 1. In this case, Text begins at position 0 and ends at position <i>|Text|</i> − 1 (<i>|Text|</i> denotes the number of symbols in <i>Text</i>). For example, if <i>Text</i> = GACCATACTG, then <i>Text</i>(4, 3) = ATA. Note that the last <i>k</i>-mer of Text begins at position <i>|Text|</i> − k, e.g., the last 3-mer of GACCATACTG starts at position 10 − 3 = 7. This discussion results in the following pseudocode for computing <i>Count(Text, Pattern)</i>.</p>



<pre>
<strong>PatternCount(<i>Text, Pattern</i>)
    <i>count</i> ← 0
    for i ← 0 to |Text| − |Pattern|
        if Text(i, |<i>Pattern</i>|) = Pattern
            <i>count ← count</i> + 1
    return <i>count</i></strong>
</pre>

<strong>Implement PatternCount</strong>

<ol>
<p><strong>Given : </strong>{DNA strings}} <i>Text</i> and <i>Pattern</i>.</p>
<p><strong>Return : </strong><i>Count(Text, Pattern)</i>.</p>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Sample Dataset</strong></p>
<pre>
<strong>GCGCG
GCG</strong>
</pre>
<p><strong class="example"> Sample Output</strong></p>
<pre>
<strong>2</strong>
</pre>
