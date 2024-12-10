add_library( day07cu day07.cpp day07.cu )

target_include_directories(day07cu PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day07cu TBB::tbb )