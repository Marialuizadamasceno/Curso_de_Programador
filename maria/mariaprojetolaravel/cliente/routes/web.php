<?php

use Illuminate\Support\Facades\Route;
use  App\Http\Controllers\Controller;
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', [Controller::class,'index'])->name('index');
Route::get('endereco', [Controller::class,'endereco'])->name('endereco');
Route::post('criar/endereco', [Controller::class,'criar'])->name('criar');
Route::get('cliente', [Controller::class,'cliente'])->name('cliente');
Route::get('editar/{id}', [Controller::class,'editar'])->name('editar');
Route::post('atualizar/{id}', [Controller::class,'atualizar'])->name('atualizar');
Route::get('delete/{id}', [Controller::class,'delete'])->name('delete');
