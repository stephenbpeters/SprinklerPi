<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Sprinkler on!</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap Cerulean theme from bootswatch.com -->
    <link rel="stylesheet" href="https://bootswatch.com/5/cerulean/bootstrap.css">
    <link rel="stylesheet" href="assets/css/font-awesome.min.css">
    <link rel="stylesheet" href="assets/css/custom.min.css">
    <link rel="stylesheet" type="text/css" href="assets/css/style.css">

</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="spacer">
                    <p>&nbsp;</p>
                    <h1>Let's turn on our sprinklers!</h1>
                    <hr>
                </div>
                <div class="row">
                <p>
We've given the turn on command.
</p>
<p>&nbsp;</p>
<p>
<a href="index.html">
...or click here to go to our main sprinkler control page</a>
</p>
<?php
$time = $_POST["time"];
$myfile = fopen("tosprinklerpi/cmd.txt", "w") or die("Unable to open file!");
$txt = "turn on/";
fwrite($myfile, $txt);
fwrite($myfile, $time);

fclose($myfile);
?>
                    </div>
                    <div class="col-md-3">
                    </div>
                    
                </div>
            </div>
        </div>


        <footer class="footer">
            <div class="container">
                <center><br><span class="text-muted">Thanks for visiting<br>
For more information visit <a href="http://www.tikimojo.com" target="_blank">http://www.tikimojo.com</a>
                </span></center>
            </div>
        </footer>

</body>

</html>