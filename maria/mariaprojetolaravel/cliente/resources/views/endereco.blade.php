<!DOCTYPE html>
<html lang="pt-br">
  <head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <title>TASKTASK</title>
    <meta charset="utf-8">
  </head>
  <body>
    

<table class="table table-striped table-dark">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">cep</th>
      <th scope="col">rua</th>
      <th scope="col">bairro</th>
      <th scope="col">cidade</th>
      <th scope="col">numero</th>
      <th scope="col">complemento</th>
    </tr>
  </thead>
  <tbody>
    @foreach ($endereco as $endereco)
    <tr>
      <th>{{$endereco->id}}</td>
      <th>{{$endereco->cep}}</td>
      <th>{{$endereco->rua}}</td>
      <th>{{$endereco->bairro}}</td>
      <th>{{$endereco->cidade}}</td>
      <th>{{$endereco->numero}}</td>
      <th>{{$endereco->complemento}}</td>
      
    

    </tr>
    @endforeach
  </tbody>
</table>
</body>
</html>