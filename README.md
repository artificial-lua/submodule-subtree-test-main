# submodule-subtree-test

git의 submodule과 subtree를 테스트하기 위한 프로젝트, 메인 저장소

# how to use

```
git clone https://github.com/artificial-lua/submodule-subtree-test-main.git main --recurse-submodules
```

위 방법으로 main 저장소를 다운로드

# Submodule

다른 git을 메인 git에서 관리하지 않으면서 사용할 수 있음
module의 커밋id를 메인 저장소가 관리하여 버전을 바꿀 수 있음

## submodule add

```
git submodule add <git-repository-url> [path/submodule-name | 미 지정 시 자동으로 생성됨]
```
