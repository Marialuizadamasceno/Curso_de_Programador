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
  <table class="table table-striped table-dark">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">nome</th>
      <th scope="col">email</th>
      <th scope="col">telefone</th>
    </tr>
  </thead>
  <tbody>
    @foreach ($cliente as $cliente)
    <tr>
      <th>{{$cliente->id}}</td>
      <th>{{$cliente->nome}}</td>
      <th>{{$cliente->email}}</td>
      <th>{{$cliente->telefone}}</td>
      
    </tr>
    @endforeach
  </tbody>
</table>
</body>
</html>