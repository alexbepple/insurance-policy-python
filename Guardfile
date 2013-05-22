notification :off

guard 'shell' do
  watch(/^(src|test).*.py$/) {|m| `nosetests --with-yanc test/unit` }
end
