<?php

namespace App\Http\Controllers;

use App\models\Cliente;
use App\models\Endereco;
use Illuminate\Http\Request;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Support\Facades\DB;

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
        $cliente = DB::table('cliente')
        ->join('endereco', 'endereco.id', '=', 'cliente.endereco_id')
        ->select('cliente.id', 'cliente.nome', 'cliente.email', 'cliente.telefone', 'endereco.cep', 'endereco.rua', 'endereco.bairro', 'endereco.cidade', 'endereco.estado', 'endereco.numero', 'endereco.complemento')
        ->get();
        return view('cliente', compact('cliente'));
    }
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;
    public function editar($id){
        $cliente = DB::table('cliente')
        ->join('endereco', 'endereco.id', '=', 'cliente.endereco_id')
        ->select('cliente.id', 'cliente.nome', 'cliente.email', 'cliente.telefone', 'endereco.cep', 'endereco.rua', 'endereco.bairro', 'endereco.cidade', 'endereco.estado', 'endereco.numero', 'endereco.complemento')
        ->where('cliente.id',$id)
        ->get();
        return view('editar', compact('cliente'));
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
        return redirect() ->route('cliente')->with('success','Cadastrado com sucesso');
        



    }
    public function atualizar(Request $request,$id){

        $cliente= Cliente::find($id);
        $cliente->nome=$request->input('nome');
        $cliente->telefone=$request->input('telefone');
        $cliente->email=$request->input('email');
        $cliente->update();

        $endereco=  Endereco::find ($cliente->endereco_id);
        $endereco->cep = $request->input('cep');
        $endereco->rua = $request->input('rua');
        $endereco->bairro = $request->input('bairro');
        $endereco->cidade = $request->input('cidade');
        $endereco->numero = $request->input('numero');
        $endereco->complemento = $request->input('complemento');
        $endereco->estado = $request->input('uf');
        $endereco->update();
        return redirect() ->route('cliente')->with('success','Atualizado com sucesso');
    }
}