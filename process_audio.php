<?php
  if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Allow: POST');
    http_response_code(405);
    exit('Method Not Allowed');
  }  
  header('Access-Control-Allow-Methods: POST');
  $data = $_POST['audio_data'];
  $file = $_POST['audio_filename'];

  $filepath = '~' . $file;

  $decodedData = base64_decode($data);
  file_put_contents($filepath, $decodedData);
?>
