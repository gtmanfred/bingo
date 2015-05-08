var myApp = angular.module('bingo', []);

myApp.controller('BingoController', ['$scope', '$log', '$http', function($scope, $log, $http) {
  $scope.rule = "test"
  $scope.ruleForm = {
      "name": "",
      "value": "",
  };
  function get_rules(){
    $http.get('/rules').
      success(function(data, status, headers, config) {
        $scope.rules = data['rules'];
      }).error(function(error) {
        $log.log(error);
      });
    $log.log($scope.rules);
  };
  function reset_buttons(){
    for(var rule in $scope.rules) {
      if ($scope.rules[rule].active) {
        $http.put('/rules/' + rule).
          success(function(data, status, headers, config) {
              get_rules();
          }).error(function(error){$log.log(error);});
      };
    }
  };
  $scope.entry = function() {
    $http.post('/rules', data=$scope.ruleForm).
      error(function(error){$log.log(error)});
  }
  $(document).on("click", "button.rule", function () {
    $http.put('/rules/' + this.name).
      success(function(data, status, headers, config) {
          get_rules();
      }).error(function(error){$log.log(error);});
  });
  $(document).on("click", "button.reset", function () {
    reset_buttons();
  });
  get_rules();
  setInterval(function(){get_rules()}, 5000);
}]);
