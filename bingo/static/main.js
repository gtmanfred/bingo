var myApp = angular.module('bingo', []);

myApp.controller('BingoController', ['$scope', '$log', '$http', function($scope, $log, $http) {
  function get_rules(){
    $http.get('/rules').
      success(function(data, status, headers, config) {
        $scope.rules = data['rules'];
      }).error(function(error) {
        $log.log(error);
      });
  };
  $(document).on("click", "button.rule", function () {
      $http.put('/rules/' + this.name).
        success(function(data, status, headers, config) {
            get_rules();
        }).error(function(error){$log.log(error);});
  });
  get_rules();
}]);
