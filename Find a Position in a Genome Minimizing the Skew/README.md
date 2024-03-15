
<h2><a href="https://rosalind.info/problems/ba1f/">Find a Position in a Genome Minimizing the Skew</a></h2>

<p>Define the <strong>skew</strong> of a DNA string Genome, denoted Skew(Genome), as the difference between the total number of occurrences of 'G' and 'C' in Genome. Let Prefix i (Genome) denote the <strong>prefix</strong> (i.e., initial substring) of Genome of length i. For example, the values of Skew(Prefix i("<strong>CATGGGCATCGGCCATACGCC</strong>")) are:</p>
<p>0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2</p>

<p><strong class="example">Minimum Skew Problem</strong></p>
<p>Find a position in a genome minimizing the skew.</p>

<p><strong>Given : </strong> A DNA string Genome.</p>
<p><strong>Return : </strong> All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).</p>



<p>&nbsp;</p>
<p><strong class="example">Sample Dataset</strong></p>
<pre>
<strong>CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG</strong>
</pre>
<p><strong class="example">Sample Output</strong></p>
<pre>
<strong>53 97</strong>
</pre>
