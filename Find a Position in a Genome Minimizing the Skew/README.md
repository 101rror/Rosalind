<h2><a href="https://rosalind.info/problems/ba1f/">Find a Position in a Genome Minimizing the Skew</a></h2>

<p>&nbsp;</p>
<p><strong class="example"></strong></p>

<p>Define the <strong>skew</strong> of a DNA string <i>Genome</i>, denoted <i>Skew(Genome)</i>, as the difference between the total number of occurrences of 'G' and 'C' in <i>Genome</i>. Let Prefix<sub>i</sub> <i>(Genome)</i> denote the <strong>prefix</strong> (i.e., initial substring) of <i>Genome</i> of length <i>i</i>. For example, the values of <i>Skew(Prefix<sub>i</sub></i> ("<i>C</i>AT<strong>GGG</strong><i>C</i>AT<i>C</i><strong>GG</strong><i>CC</i>ATA<i>C</i>G<i>CC</i>")) are:</p>
<p>0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2</p>

<p><strong class="example">Minimum Skew Problem</strong></p>
<p><i>Find a position in a genome minimizing the skew.</i></p>

<ol>
<p><strong>Given : </strong> A DNA string <i>Genome.</i></p>
<p><strong>Return : </strong> All integer(s) <i>i</i> minimizing <i>Skew(Prefix<sub>i</sub> (Text))</i> over all values of <i>i</i> (from 0 to |<i>Genome</i>|).</p>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Sample Dataset</strong></p>
<pre>
<strong>CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG</strong>
</pre>
<p><strong class="example"> Sample Output</strong></p>
<pre>
<strong>53 97</strong>
</pre>
