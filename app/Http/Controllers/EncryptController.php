<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;

class EncryptController extends Controller {

    public function __construct() {
        //
    }

    public function encrypt(Request $request) {
        $data=$request->input('data');
        $encrypt=new \Sovit\TikTokApp\Encrypt();
        $output=$encrypt->encrypt($data);
        return response()->json(['base64_value'=>base64_encode($output)]);
    }
}
