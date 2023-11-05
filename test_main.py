from main import main

def test_main():
  # test that after main is run, the outputs.md file contatains stuff we want
  main()
  with open("outputs.md", "r") as f:
    contents = f.read()
    #  "Spark session created"
    assert "Spark session created" in contents
    # "Data loaded"
    assert "Data loaded" in contents
    # "Query executed "
    assert "Query executed: " in contents
    # "Data transformed"
    assert "Data transformed" in contents
    # "Spark session stopped"
    assert "Spark session stopped" in contents
  
