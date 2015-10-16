<?php

$servername = "localhost";
$username = "deb15015n2_photo";
$password = "";
$dbname = "deb15015n2_photo";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
$sql = "SELECT id, user, url FROM photo ORDER BY id DESC LIMIT 5";
$result = $conn->query($sql);

$json = [];

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
    	array_push($json, $row);
    }
    echo json_encode($json);
} else {
    echo "0 results";
}
$conn->close();
?>