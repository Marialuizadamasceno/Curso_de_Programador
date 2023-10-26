<?php

namespace App\Http\Controllers;

use App\models\Cliente;
use App\models\Endereco;
use Illuminate\Http\Request;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;
    public function index(){
        return view('welcome');
    }
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;
    public function endereco(){
        $endereco=Endereco::all();
        return view('endereco', compact('endereco'));
    } 
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;
    public function cliente(){
        $cliente=Cliente::all();
        return view('cliente', compact('cliente'));
    }

    public function criar(Request $request){
        $endereco= new Endereco();
        $endereco->cep = $request->input('cep');
        $endereco->rua = $request->input('rua');
        $endereco->bairro = $request->input('bairro');
        $endereco->cidade = $request->input('cidade');
        $endereco->numero = $request->input('numero');
        $endereco->complemento = $request->input('complemento');
        $endereco->estado = $request->input('uf');
        $endereco->save();

        $cliente=new Cliente();
        $cliente->nome=$request->input('nome');
        $cliente->telefone=$request->input('telefone');
        $cliente->email=$request->input('email');
        $cliente->endereco_id=$endereco->id;
        $cliente->save();
        



    }
}