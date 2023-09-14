<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>While practice</title>
</head>

<body>
    <form name="form" action="" method="post">
        N: <input type="number" name="limit" id="limit">
        <input type="submit" value="Calcula series">
    </form>
    <h1>Serie 19:</h1>
    <?php
    if (isset($_POST['limit'])) {
        $n = $_POST['limit'];
        $i = 3;
        $x = 0;
        while ($i <= $n) {
            if ($i % 2 == 1) {
                $x += $i / 3;
            }
            $i++;
        }
        echo $x;
    }
    ?>
    <h1>Serie 20:</h1>
    <?php
    if (isset($_POST['limit'])) {
        $n = $_POST['limit'];
        $i = 1;
        $x = 0;
        while ($i <= $n) {
            $x += (2 + 2 + 1 / 2);
            $i++;
        }
        echo $x;
    }
    ?>
    <h1>Serie 21:</h1>
    <?php
    if (isset($_POST['limit'])) {
        $n = $_POST['limit'];
        $i = 1;
        $x = 0;
        while ($i <= $n) {
            $x += $i;
            $i++;
        }
        echo $x;
    }
    ?>
    <h1>Serie 22:</h1>
    <?php
    if (isset($_POST['limit'])) {
        $n = $_POST['limit'];
        $i = 1;
        $x = 0;
        while ($i <= $n) {
            if ($i % 3 == 0) {
                $x += 1 / 2;
            } else {
                $x += $i;
            }
            $i++;
        }
        echo $x;
    }
    ?>
    <form name="function_form" action="" method="post">
        Desde: <input type="number" name="from" id="from">
        Hasta: <input type="number" name="to" id="to">
        <input type="submit" value="Imprimir tabla">
    </form>

    <table border="1">
        <tr>
            <th>z = x^2 / 3</th>
        </tr>
        <tr>
            <th>x</th>
            <th>z</th>
        </tr>
        <?php
        if (isset($_POST['from']) && isset($_POST['to'])) {
            $from = $_POST['from'];
            $to = $_POST['to'];
            if ($from < $to) {
                while ($from <= $to) {
                    $z = round(pow($from, 2) / 3, 6);
                    echo "<tr><td>$from</td><td>$z</td></tr>";
                    $from += 3;
                }
            } else {
                echo "El primer numero tiene que ser menor al segundo, intente de nuevo";
            }
        }
        ?>
    </table>
</body>

</html>