<h1>Cryptographic Logic for Easy-to-Access and Rememberable (CLEAR) Keys</h1>
<h2>Overview</h2>
<p>
  This cryptographic scheme, while still in its early stages, aims at a secure encryption mechanism that eliminates the possibility of malicious actors gaining access to the key.
  <br>
  For a long while, we've come to rely on the security provided by complicated keys and their algorithms to keep our data safe and secure.
  But what guarantees the safety of these keys themselves? Surely, they have to be stored somewhere digital, and we, as humans, are quite possibly just a click away from infecting our devices.
  <br>
  To combat this issue, I've come up with an idea for a new symmetric cryptographic scheme that makes it such that the key is ONLY ten digits long, making the process of remorising your key no more difficult that memorising a phone number.
</p>
<h2>Version 1</h2>
<p>
  CLEAR Keys V1 builds on the concept of Multivariate Polynomial Expressions, and its security primarily depends on the difficulty of solving such equations without additional input, i.e, the key.
</p>
<h3>Encryption</h3>
<p>
  V1 works by taking five variables of two digits each, and the Unicode value of each character to be encrypted, and evaluates a pair of encrypted values from a pair of hexavariable quadratic expressions.
  These five 2-digit numbers, form the key.
</p>
<h3>Decryption</h3>
<p>
  The decryption process involves the simplification of the hexavariable quadratic equations into a pair of monovariable quadratic equations by providing the key and respective encrypted values.
  The equations are now solved and owing to the fact that the equations are quadratic in nature, each will return a pair of values, the only common element being the correct Unicode value of the now decrypted character.
  The common element is extracted and converted back to the character.
</p>
<h2>Version 2</h2>
<p>
  V2 is still under development.
  <br>
  V2 aims at converting the expressions into heptavariable quadratic expressions, by introducing a 128 digit variable that need not be memorised, stored, or shared.
  Its aim is to increase the keyspace for possible combinations, reducing the likelyhood of a successful brute-force attack, and generally increasing the complexity of the equations.
</p>
<h2>Testing</h2>
<p>
  Anyone, if interested, is requested to test this cryptographic scheme for flaws, possible vulnerabilities, and reconsiderations to make, if any.
  <br>
  You may reach out to me via email and/or discord.
  <br>
  Email: hrishav.saha@gmail.com
  <br>
  Discord: lonewolf1999
</p>
