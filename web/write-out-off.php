<html>
<head>
</head>
<body>
<p>
<strong>Sprinkler off!</strong>
<br>
<br>
We have sent the command to turn the sprinkler off.
</p>
<p>
<br>
<a href="index.html">
click here to go to sprinkler control page
</a>
</p>


<?php
$foo = $_POST["name"];
$myfile = fopen("tosprinklerpi/cmd.txt", "w") or die("Unable to open file!");
$txt = "turn off";
fwrite($myfile, $txt);
# turn off for now fwrite($myfile, $foo);
$txt3 = "Minnie Mouse\n";
# turn off for now fwrite($myfile, $txt3);
fclose($myfile);
?>

</body>
</html>

