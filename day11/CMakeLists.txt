add_library( day11 day11.cpp)

target_include_directories(day11 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day11 TBB::tbb )