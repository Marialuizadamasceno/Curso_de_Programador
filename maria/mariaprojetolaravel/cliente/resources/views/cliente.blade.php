<!DOCTYPE html>
<html lang="pt-br">
  <head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <title>TASKTASK</title>
    <meta charset="utf-8">
  </head>
  <body>
  </div>
      <div class="col-12">
        <a href="{{route('index')}}"><button type="submit" class="btn btn-primary">novo cadastro</button></a>
      </div>
    <br>
    @if(session('success'))
    <div class="alert alert-success">
      {{session('success')}}
</div>
    @endif
  <table class="table table-striped table-dark">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">nome</th>
      <th scope="col">email</th>
      <th scope="col">telefone</th>
      <th scope="col">cep</th>
      <th scope="col">rua</th>
      <th scope="col">bairro</th>
      <th scope="col">cidade</th>
      <th scope="col">numero</th>
      <th scope="col">complemento</th>
      <th scope="col">Ação</th>
      
     


      </div>

    </tr>
  </thead>
  <tbody>
    @foreach ($cliente as $cliente)
    <tr>
      <th>{{$cliente->id}}</td>
      <th>{{$cliente->nome}}</td>
      <th>{{$cliente->email}}</td>
      <th>{{$cliente->telefone}}</td>
      <th>{{$cliente->cep}}</td>
      <th>{{$cliente->rua}}</td>
      <th>{{$cliente->bairro}}</td>
      <th>{{$cliente->cidade}}</td>
      <th>{{$cliente->numero}}</td>
      <th>{{$cliente->complemento}}</td>
      <th>
      <div class="btn-group" role="group" aria-label="Basic mixed styles example">
      <a href="{{route('editar',$cliente->id)}}"><button type="button" class="btn btn-danger">editar</button></a>
      <a href="{{route('delete',$cliente->id)}}">
  <button type="button" class="btn btn-warning">excluir</button></a>
</div>
</div></td>

      
    </tr>
    @endforeach
  </tbody>
</table>
</body>
</html>