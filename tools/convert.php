<?php

/**
 * 将 https://github.com/overtrue/pinyin 中的词库转换为phrase.db
 */

include "./src/Pinyin/Pinyin.php";

use Overtrue\Pinyin\Pinyin;

$filepath = dirname(__DIR__).'/pinyin/src/data/dict.php';

// echo __DIR__ . "\n";
// echo $filepath . "\n";

$dict = json_decode(file_get_contents($filepath), true);

$result = '';

foreach ($dict as $word => $pinyin) {
    if ( mb_strlen($word, 'utf-8') > 1 && 3 == strlen($word) / mb_strlen($word, 'utf-8') ) {
        $pinyin = str_replace(' ', ',', Pinyin::trans($word)); 
        $result = $result . $word . '=' . $pinyin . "\n";
    }
}  

echo "convert ... \n";

$fh = fopen('./phrase.db', "w");
fwrite($fh, $result); 
fclose($fh);

