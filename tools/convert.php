<?php
include "./src/Pinyin/Pinyin.php";

use Overtrue\Pinyin\Pinyin;

$filepath = dirname(__DIR__).'/dict.php';

// echo __DIR__ . "\n";
// echo $filepath . "\n";

$dict = json_decode(file_get_contents($filepath), true);

$result = '';

foreach ($dict as $word => $pinyin) {
    if ( mb_strlen($word, 'utf-8') > 1 && 3 == strlen($word) / mb_strlen($word, 'utf-8') ) {

        // 有些短语是`一分耕耘，一分收获`这种类型，处理一下
        if (strpos($word, '，') !== false) {
            $pinyin = Pinyin::trans($word);
            $words = explode('，', $word);
            $pinyins = explode(',', $pinyin);
            for($i=0; $i<count($words); ++$i) {
                $w = $words[$i];
                $p = trim($pinyins[$i]);
                $p = str_replace(' ', ',', $p);
                $result = $result . $w . '=' . $p . "\n";
            }

        } else {
            $pinyin = str_replace(' ', ',', Pinyin::trans($word)); 
            $result = $result . $word . '=' . $pinyin . "\n";
        }
    }
}  

echo "convert ... \n";

$fh = fopen('./phrase.db', "w");
fwrite($fh, $result); 
fclose($fh);

